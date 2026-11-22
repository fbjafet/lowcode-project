# Multimodal Public Transit Disruption & Passenger notification Engine — Specification
 
## Purpose
A dispatcher dashboard that monitors operations, detects route disruptions, and automates multi-channel passenger alerts (web, SMS).
 
## Entities
### Route (`routes`)
- id (integer, primary key)
- route_code (text, required, unique, max 20)
- name (text, required, max 150)
- mode (one of: bus, rail, tram — required)
- status (one of: normal, delayed, diverted, suspended — default normal)

### Stop (`stops`)
- id (integer, primary key)
- stop_code (text, required, unique, max 20)
- name (text, required, max 150)
- latitude (float, required)
- longitude (float, required)
- has_digital_signage (boolean, default false)

### Trip (`trips`)
- id (integer, primary key)
- route_id (integer, foreign key -> routes.id, required)
- headsign (text, required, max 150)
- scheduled_departure (timestamp, required)
- delay_minutes (integer, default 0)
- status (one of: scheduled, active, delayed, cancelled — default scheduled)

### DisruptionEvent (`disruption_events`)
- id (integer, primary key)
- route_id (integer, foreign key -> routes.id, required)
- affected_stop_id (integer, foreign key -> stops.id, optional)
- raw_driver_note (text, required)
- severity (one of: minor, major, critical — default minor)
- diversion_summary (text, optional)
- status (one of: open, resolved — default open)
- created_at (timestamp)
- resolved_at (timestamp, optional)

### ServiceAlert (`service_alerts`)
- id (integer, primary key)
- disruption_id (integer, foreign key -> disruption_events.id, required)
- channel (one of: web, sms, signage — required)
- tone (one of: urgent, informational — required)
- message_body (text, required, max 500)
- status (one of: draft, published, archived — default draft)
- published_at (timestamp, optional)

## Routes

| Method | Path | Does |
|---|---|---|
| GET | / | Dispatcher dashboard: active disruptions, route statuses, live feed |
| GET | /routes | List all routes and current operational status |
| GET | /routes/<id> | Show route details, stops, upcoming trips, and active disruptions |
| GET | /disruptions/new | Form to ingest a driver note or operational alert |
| POST | /disruptions | Create disruption event, extract AI impact & diversion notice, redirect to /disruptions/<id> |
| GET | /disruptions/<id> | Show disruption details, diversion notice, and drafted multi-channel alerts |
| POST | /disruptions/<id>/alerts | Draft or regenerate AI alerts across channels (web, SMS, signage) for a chosen tone |
| POST | /alerts/<id>/publish | Mark alert as published and broadcast update, redirect back |
| POST | /disruptions/<id>/resolve | Mark disruption resolved, reset route status, redirect to / |
| GET | /events/stream | Server-Sent Events (SSE) stream for real-time dashboard updates |

## Technical constraints
- Python 3.11+, Flask 3.x
- SQLAlchemy 2.0 with PostgreSQL (read/write engine split configured for read-replica timetable lookups)
- Jinja2 templates in `templates/`, extending a single `base.html`
- Server-Sent Events (SSE) for real-time dispatch updates using minimal vanilla JS (no frontend JS framework)
- LLM API integration isolated in a service module for impact extraction, diversion notices, and tone-profiled copy
- Seed script generating GTFS-adjacent routes, stops, trips, simulated delays, and incident logs
- Modular repository structure (`app/`, `models/`, `routes/`, `services/`, `seeds/`, `docs`)
- No authentication

## Out of scope
User accounts & role permissions · live GPS/AVL vehicle telemetry · real SMS/signage hardware delivery (simulated publish log only) · public passenger-facing portal · multi-language translation · historical analytics
