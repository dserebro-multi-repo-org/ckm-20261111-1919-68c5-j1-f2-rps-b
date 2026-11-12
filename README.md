# Rock Paper Scissors REST API
[![Created with Morph](https://img.shields.io/badge/created%20with-Morph-6E56CF)](https://modelcode.ai)

A Rock Paper Scissors game exposed as a REST API, built with PHP and Symfony.

## Prerequisites

- PHP >= 8.2 (note: the versions pinned in `composer.lock` may require PHP 8.4; use PHP 8.4 if `composer install` reports a platform requirement error)
- PHP extensions: xml, mbstring, curl, zip
- [Composer](https://getcomposer.org/)
- [Symfony CLI](https://symfony.com/download) (optional, for the dev server)

### Install prerequisites (macOS)

```bash
brew install php composer symfony-cli/tap/symfony-cli
```

## Install

```bash
composer install
```

## Run

```bash
# Using Symfony CLI
symfony server:start

# Or using PHP's built-in server
php -S localhost:8000 -t public/
```

## Overview

This API lets two players play Rock Paper Scissors. A client creates a game, then each player submits a move; once both moves are in, the API reports the result.

Endpoints:

- `POST /games` — create a new game.
- `POST /games/{id}/moves` — submit a player's move for the given game.

Main components:

- `src/Controller/` — `GameController` defines the HTTP routes and turns requests and responses into JSON.
- `src/Entity/` — `Game` is the game model that is serialized in API responses.
- `src/Service/` — `GameService` holds the game logic: creating games, recording moves, determining the winner, and loading and saving game state.

## Testing

There are no automated tests in this repository yet: it has no `tests/` directory and no test framework is configured in `composer.json`.

To verify the API manually, start the server (see [Run](#run)) and call the endpoints with `curl`:

```bash
# Create a game
curl -X POST http://localhost:8000/games

# Submit a move (replace {id} with the id returned above)
curl -X POST http://localhost:8000/games/{id}/moves \
  -H 'Content-Type: application/json' \
  -d '{"player": 1, "choice": "rock"}'
```

## Configuration

Environment variables are read from `.env` (override locally in an untracked `.env.local`).

| Variable | Required | Purpose |
| --- | --- | --- |
| `APP_ENV` | Yes | Symfony environment (`dev` by default). |
| `APP_DEBUG` | No | Enables debug mode (`true` by default in `.env`). |
| `APP_SECRET` | Yes | Symfony secret; replace the placeholder with a random value outside development. |

Game state is stored in `var/data/games.json`, created automatically at runtime. No database is needed.

## Project layout

- `config/` — Symfony configuration and routes.
- `public/` — web entry point (`index.php`).
- `src/` — application code (`Controller/`, `Entity/`, `Service/`).
