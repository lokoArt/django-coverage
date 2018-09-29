### Install dependencies
```pip install -r requirements.txt```

### Run
This command will start a local server on 8000 port

```./manage.py runserver```

Documentation is available by [http://127.0.0.1:8000/docs/](http://127.0.0.1:8000/docs/) 


### Example of the payload
```json{
  "airplanes": [
    {
      "id": 100,
      "passengers_number": 100
    },
    {
      "id": 50,
      "passengers_number": 75
    },
    {
      "id": 70,
      "passengers_number": 87
    },
    {
      "id": 98,
      "passengers_number": 123
    },
    {
      "id": 1000,
      "passengers_number": 215
    },
    {
      "id": 1111,
      "passengers_number": 15
    },
    {
      "id": 155,
      "passengers_number": 31
    },
    {
      "id": 654,
      "passengers_number": 99
    },
    {
      "id": 12315,
      "passengers_number": 64
    },
    {
      "id": 8888,
      "passengers_number": 400
    }
  ]
}
```

### Run tests
```sh
coverage run manage.py test
covereage report
```