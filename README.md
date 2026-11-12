# Rock Paper Scissors REST API

A Rock Paper Scissors game exposed as a REST API, built with PHP and Symfony.

## Prerequisites

- PHP >= 8.2
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
