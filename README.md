# How to run in virtual environment (venv) in local host

1. cd path/to/project # cd to the directory where requirements.txt is located.</br>
2. python -m venv path/to/project # creates a virtual in where requirements.txt is located.</br>
2. .\Scripts\activate</br> 
3. pip install -r requirements.txt</br>
4. set FLASK_APP=prediction_alternative</br>
5. set FLASK_ENV=development
6. flask run
7. POSTMAN to http://127.0.0.1:5000/ with POST. With the body parameters set to form. Then the key = image, value = select a file.
8. Upload an image of any singapore food in jpg or png (IMPORTANT) and send request.
