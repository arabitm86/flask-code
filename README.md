# flask-code

minikube addons enable ingress

helm install flask-blog ./flask-chart/

kubectl expose deployment flask-blog --type=NodePort --port=5000

minikube service flask-blog --url

## need to figure out how to add ingress via helm

