@ECHO OFF 
set FLASK_APP=project.app
set FLASK_ENV=development
set DEBUG=true
set JWT_SECRET_KEY="7b69f55b6d91eb72206525bdc197b343f440cc63a440a0f83a81a92eae642bb4"

SET DB_NAME=plant_disease_prediction
SET DB_URL=localhost
SET DB_USER=root
SET DB_PWD=smartforum123
SET DB_PORT=3306

CMD /k "python -B runDebug.py"
