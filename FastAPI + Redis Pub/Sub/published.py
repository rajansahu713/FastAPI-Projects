import json
import time
import redis
import random

REDIS_URL = "redis://localhost:6379/0"
CHANNEL = "ipl-score"


client = redis.Redis.from_url(REDIS_URL)

# Fake over-by-over simulation
import random

def simulate_innings(score):
    runs_this_over = random.randint(0, 20)
    wickets_this_over = random.randint(0, 2)

    # Remaining wickets
    remaining = 10 - score["wickets"]
    wickets_this_over = min(wickets_this_over, remaining)

    # Update score
    score["runs"] += runs_this_over
    score["wickets"] += wickets_this_over
    score["overs"] +=1

    # Commentary
    score["commentary"].append(
        f"Over {score["overs"]}: {runs_this_over} runs, {wickets_this_over} wicket(s)"
    )

    # Stop if all out
    if score["wickets"] == 10:
        score["game_over"] = True
        score["commentary"].append("All out! Innings over.")
    
    return score


def publish_score(data):
    client.publish(CHANNEL, json.dumps(data))


if __name__ == "__main__":
    score = {
        "team": "MI",
        "runs": 0,
        "wickets": 0,
        "overs": 0,
        "commentary": [],
        "game_over": False
    } 
    for _ in range(20):
        score_data = simulate_innings(score)
        # publish to redis
        publish_score(score_data)
        
        if score_data["game_over"]:
            break

        time.sleep(3)
