import ReactPlot from 'react-plotly.js'
import { Dataframe } from '../interfaces/api.interface'

interface Data {
  data: Dataframe
}

export default function Plot({ data }: Data) {
  return (
    <ReactPlot 
      data={[{
        x: data.x,
        y: data.y
      }]}
      layout={{
        width: 950, 
        height: 400,
        title: `Resultados - Correlacion: ${data.correlation}%`, 
        xaxis: {
          title: data.labels[0],
        },
        yaxis: {
          title: data.labels[1],
          gridcolor: "#475569"
        },
        paper_bgcolor: "#1e293b",
        plot_bgcolor: "#1e293b",
        font: {
          color: "white"
        }
      }}
    />
  )
}
