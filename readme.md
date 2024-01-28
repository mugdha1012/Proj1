
# Flask Wrapper for interact.sh

This service provides a simple API wrapper for `interact.sh`, offering two primary endpoints to interact with an interact.sh server.

## API Endpoints

1. **GET `/api/getURL`**
   - Retrieves the URL of the testing server being used in the current interact.sh session.

2. **GET `/api/getInteractions`**
   - Accepts the URL of the testing server and returns information about its interactions, including caller IP and timestamps.
   - Optionally, timestamp limits can be specified to filter the interactions.

## Setup and Usage

1. Ensure Python 3.8+ and Flask are installed.
2. Clone the repository
3. Run the Flask application:
   ```bash
   python app.py
   ```
4. The application will start on `http://localhost:5000`.

The application is now accessible at `http://localhost:5000`.

