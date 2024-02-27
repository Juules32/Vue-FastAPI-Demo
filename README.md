# How to run
Start new terminal and go to `backend`:
- `pip install -r requirements.txt`
- `uvicorn main:app --reload`

Start new terminal and go to `frontend`:
- `npm i`
- `npm run dev`

Go to [localhost:8080](http://localhost:8080). Clicking the button sends a request to the backend and should return an appropriate response.

Going to [localhost:8000/answer](http://localhost:8000/answer) Should show the response in json.

Going to [localhost:8000/docs](http://localhost:8000/docs) Should show documentation for each API endpoint. These can also be interacted with.
