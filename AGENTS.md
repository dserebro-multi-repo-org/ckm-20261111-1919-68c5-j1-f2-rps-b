# AGENTS.md

Symfony REST API for Rock Paper Scissors. No database; state lives in `var/data/games.json`.

## Commands
- Install: `composer install` (`composer.lock` may need PHP 8.4; PHP >= 8.2 is declared).
- Build: none.
- Run: `php -S localhost:8000 -t public/` (or `symfony server:start`).
- Lint: none configured.
- Test: no automated tests or `tests/` directory exist. Verify manually with `curl`:
  - `curl -X POST http://localhost:8000/games` (expects 201)
  - `curl -X POST http://localhost:8000/games/{id}/moves -H 'Content-Type: application/json' -d '{"player": 1, "choice": "rock"}'`

## Layout
- `src/Controller/GameController.php` — routes (PHP attributes) and JSON responses only.
- `src/Service/GameService.php` — game logic and JSON file persistence.
- `src/Entity/Game.php` — game model (`toArray()` for responses).
- `config/` — Symfony config; `public/index.php` — entry point.

## Conventions
- Controllers catch exceptions and return JSON `{"error": "..."}`: `InvalidArgumentException` -> 422, "not found" `RuntimeException` -> 404, otherwise 500.
- Services throw `InvalidArgumentException` for bad input and `RuntimeException` for missing games.
- Log through the injected `LoggerInterface`; use constructor injection with `readonly` properties.
- Moves are `rock`, `paper`, `scissors`; players are `1` or `2`.

## Gotchas
- Do not commit secrets; `APP_SECRET` in `.env` is a placeholder.
- `var/` is runtime data; do not commit it.
- Changes to documentation should only touch `README.md`/`AGENTS.md`.
