```
python3 -m venv .venv
source .venv/bin/activate
```

```
.venv/bin/pip install -r requirements.txt
```

```
pip freeze > requirements.txt
```

```
.venv/bin/uvicorn main:app --reload
```