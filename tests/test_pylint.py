import os
import subprocess

def check_pylint_scores():
    """
    Runs pylint on all .py files in the current directory and checks if they are all rated 10/10.
    Returns a list of files that do not meet the 10/10 score along with their scores.
    """
    py_files = [f for f in os.listdir('.') if f.endswith('.py')]
    files_not_rated_10 = []

    for file in py_files:
        result = subprocess.run(['pylint', file], capture_output=True, text=True)
        output = result.stdout
        if result.returncode == 0:
            # Extract the pylint score from the output
            for line in output.split('\n'):
                if 'Your code has been rated at' in line:
                    score_line = line
                    break
            else:
                files_not_rated_10.append((file, "Score line not found in pylint output."))
                continue

            # Extract the score from the line
            try:
                score_str = score_line.split('Your code has been rated at')[1].split('/')[0].strip()
                score = float(score_str)
            except (IndexError, ValueError):
                files_not_rated_10.append((file, "Failed to parse pylint score."))
                continue

            if score != 10.0:
                files_not_rated_10.append((file, score_line))
        else:
            files_not_rated_10.append((file, output))
    
    return files_not_rated_10


def test_pylint_scores():
    """
    Test to check that all .py files are rated 10/10 by pylint.
    """
    files_not_rated_10 = check_pylint_scores()
    assert len(files_not_rated_10) == 0, f"Some files are not rated 10/10: {files_not_rated_10}"
