Prereqs: Make sure you have Docker for Desktop installed.

### clone the repo:

git clone https://github.com/angelicakhughes/craft_demo.git

### Option I:

craft_demo.sh:

Usage for craft_demo.sh: 
./craft_demo.sh AL,BE,GE,LI,FI,FO,ZZ

Use this bash script to convert country code to coutry name.


### Option II:

craft_demo.py:

Usage for craft_demo.py: 
./craft_demo.py lookup --countrycode=AL,BE,GE,LI,FI,FO,ZZ

Use this python script to convert country code to coutry name.

### Bonues: REST API Service with Flask:

usage:

sudo pip install -r requirements.txt
export FLASK_APP=main.py
python3 -m flask run
./main.py


Navigate to http://127.0.0.1:5000/

http://127.0.0.1:5000/health: returns service health

http://127.0.0.1:5000/diag: checks status code of the api https://www.travel-advisory.info/api return 

http://127.0.0.1:5000/convert: converts country code to coutry name.


### Create a container based on the Flask Docker image, then deploy to Kube cluster using MiniKube

docker login

docker build -f Dockerfile -t country-lookup:latest .
docker run -p 5001:5000 country-lookup 

Install Minikube:
brew install minikube
sudo mv minikube /usr/local/bin

cd kubernetes
kubectl apply -f deployment.yaml 
minikube start

kubectl get svc
kubectl get pods

minikube dashboard

### Set Up Basic monitoring with Promethues/Grafana:

Install Promethues using Helm:
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 chmod 700 get_helm.sh ./get_helm.sh
helm install prometheus-operator stable/prometheus-operator — namespace monitor

kubectl get pods

(select grafana pod)

Prometheus/Grafana:

kubectl port-forward prometheus-operator-grafana-6c88866f7-dn4z4 3000

navigate to: http://127.0.0.1:3000/

Select and view dashboards for Kubelets, Cluster, Pods, etc.

Credentials:
Admin
prom-operator
