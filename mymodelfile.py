import pandas as pd

class MyModel:

    def __init__(self):

        self.base_score = 55

        # Powerplay batting intent
        self.attack_rating = {
            "royal challengers bangalore": 5,
            "mumbai indians": 4,
            "kolkata knight riders": 4,
            "punjab kings": 4,
            "sunrisers hyderabad": 4,
            "rajasthan royals": 1,
            "delhi capitals": 2,
            "gujarat titans": 1,
            "lucknow super giants": 1,
            "chennai super kings": 0
        }

        # Higher = stronger PP bowling
        self.bowling_strength = {
            "chennai super kings": 3,
            "gujarat titans": 2,
            "lucknow super giants": 2,
            "rajasthan royals": 3,
            "kolkata knight riders": 1,
            "sunrisers hyderabad": 0,
            "delhi capitals": 0,
            "punjab kings": -1,
            "mumbai indians": -1,
            "royal challengers bangalore": -2
        }

    def fit(self, deliveries_df, players_df=None, matches_df=None):
        return self

    def get_venue_factor(self, venue):

        venue = str(venue).lower().strip()

        venue_map = {
            ("m chinnaswamy", "chinnaswamy", "bengaluru", "bangalore"): 8,
            ("wankhede", "mumbai"): 4,
            ("rajiv gandhi", "uppal", "hyderabad"): 6,
            ("pca", "punjab cricket association", "mohali"): 1,
            ("hpca", "dharamshala"): 5,
            ("eden gardens", "eden", "kolkata"): 2,
            ("narendra modi", "motera", "ahmedabad"): 2,
            ("arun jaitley", "feroz shah kotla", "delhi"): 2,
            ("sawai mansingh", "jaipur"): 2,
            ("ekana", "lucknow"): -5,
            ("chidambaram", "chepauk", "chennai"): -5
        }

        for aliases, value in venue_map.items():
            if any(alias in venue for alias in aliases):
                return value

        return 1

    def predict(self, test_df):

        # Handle single-column CSV input
        if len(test_df.columns) == 1:

            col = test_df.columns[0]

            test_df = test_df[col].str.split(",", expand=True)

            test_df.columns = [
                "id",
                "venue",
                "innings",
                "batting_team",
                "bowling_team",
                "batsman",
                "bowler"
            ]

        predictions = []

        for _, row in test_df.iterrows():

            venue = str(row["venue"]).lower()
            batting = str(row["batting_team"]).lower()
            bowling = str(row["bowling_team"]).lower()

            innings = int(row["innings"])

            score = self.base_score

            # Venue factor
            venue_factor = self.get_venue_factor(venue)
            score += venue_factor

            # Batting intent
            attack = self.attack_rating.get(batting, 1)
            score += attack

            # Bowling effect
            bowling_effect = self.bowling_strength.get(bowling, 0)
            score -= bowling_effect

            # Innings effect
            if innings == 1:
                score += 1
            else:
                score += 3

                # Dew advantage on batting-friendly grounds
                if venue_factor >= 4:
                    score += 2

            # Aggressive matchup
            combined_attack = (
                self.attack_rating.get(batting, 1)
                + self.attack_rating.get(bowling, 1)
            )

            if combined_attack >= 8:
                score += 3
            elif combined_attack >= 6:
                score += 2

            # Strong batting side on batting-friendly venue
            if attack >= 4 and venue_factor >= 5:
                score += 2

            # Slow pitch protection
            if venue_factor <= -4:
                score -= 2

            # Conservative normalization
            score = round(score)

            # Realistic powerplay bounds
            score = max(53, min(65, score))

            predictions.append({
                "id": int(row["id"]),
                "predicted_score": int(score)
            })

        return (
            pd.DataFrame(predictions)
            .sort_values("id")
            .reset_index(drop=True)
        )