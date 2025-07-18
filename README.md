# flintsky_residence

## Metrics

The backend exposes Prometheus metrics at `/metrics`. Install the
`kube-prometheus-stack` Helm chart to collect them and visualise in
Grafana:

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install prometheus-stack prometheus-community/kube-prometheus-stack
kubectl apply -f k8s/
```

After deployment, Grafana will pick up the `ServiceMonitor` and you can
create dashboards based on the exported metrics.
