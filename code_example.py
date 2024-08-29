from datetime import datetime

class TimeUtils:
    """
    A utility class for time-related operations.
    """

    @staticmethod
    def calculate_time_difference_in_hours(start_time, end_time):
        """
        Calculates the time difference between two datetime objects in hours.
        """
        time_diff = end_time - start_time
        return time_diff.total_seconds() / 3600


class User:
    """
    Represents a User with a name and a list of session information.
    """

    def __init__(self, name, sessions):
        self.name = name
        self.sessions = sessions

    def get_sessions(self):
        """
        Returns the user's sessions.
        """
        return self.sessions


class UserMetricsCalculator:
    """
    Calculates metrics for a user, including total login time and session count.
    """

    def __init__(self, user):
        self.user = user

    def calculate_metrics(self):
        """
        Calculates user metrics including total login time and number of sessions.

        :return: A dictionary with the calculated metrics
        """
        sessions = self.user.get_sessions()
        total_login_time = 0
        session_count = len(sessions)

        for session in sessions:
            start_time = session['start']
            end_time = session['end']

            # Calculate the time difference for each session
            total_login_time += TimeUtils.calculate_time_difference_in_hours(start_time, end_time)

        metrics = {
            'total_login_time': total_login_time,
            'session_count': session_count
        }

        return metrics


# Example usage
if __name__ == "__main__":
    user = User(
        name="John Doe",
        sessions=[
            {'start': datetime(2023, 8, 1, 9, 0, 0), 'end': datetime(2023, 8, 1, 17, 0, 0)},
            {'start': datetime(2023, 8, 2, 9, 0, 0), 'end': datetime(2023, 8, 2, 17, 0, 0)},
        ]
    )

    calculator = UserMetricsCalculator(user)
    metrics = calculator.calculate_metrics()
    print("User metrics:", metrics)
