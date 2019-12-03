# http-health

Push to artifactory and create pull secret in kubernetes:

```
docker login artifactory.thalesdigital.io
docker tag http-health:latest artifactory.thalesdigital.io/docker/runnerz/http-health:latest
docker push artifactory.thalesdigital.io/docker/runnerz/http-health:latest

kubectl -n monitoring create secret docker-registry regcred --docker-server=artifactory.thalesdigital.io --docker-username=username@thalesdigital.io --docker-password=XXXXXXXXXXXX --docker-email=username@thalesdigital.io

kubectl -n monitoring apply -f pod.yaml
```
