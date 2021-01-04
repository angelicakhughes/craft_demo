craft_demo.sh:

Usage for craft_demo.sh: ./craft_demo.sh AL,BE,GE,LI,FI

Use this bash script to convert country code to coutry name.

Alternative - 

craft_demo.py:

Usage for craft_demo.py: ./craft_demo.py lookup --countrycode=AL,BE,GE,LI,FI

REST API Service with Flask:

usage:

./main.py

sudo pip install -r requirements.txt
export FLASK_APP=main.py
flask run
Navigate to http://0.0.0.0:5000/

http://0.0.0.0:5000/health: returns service health

http://0.0.0.0:5000/diag: check status code of the api https://www.travel-advisory.info/api return 

http://0.0.0.0:5000/convert: converts country code to coutry name.


Create a container based on the Flask Docker image, then deploy to Kube cluster using MiniKube...

docker build -f Dockerfile -t country-lookup:latest .
docker run -p 5001:5000 country-lookup 

cd kubernetes
kubectl apply -f deployment.yaml 

kubectl get svc

kubectl get pods

minikube start

minikube dashboard

Set Up Basic monitoring with Promethues/Grafana:

kubectl get pods

(select grafana pod)

kubectl port-forward prometheus-operator-grafana-6c88866f7-dn4z4 3000

Credentials:

Admin

prom-operator


