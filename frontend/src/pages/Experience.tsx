import Plot from "../components/Plot"
import { useEffect, useState } from "react"
import { Api } from "../services/Api"
import { Dataframe } from "../interfaces/api.interface"

export default function Experience() {
  const [dataPlot, setDataPlot] = useState<Dataframe[]>([] as Dataframe[])

  const getPlotData = async () => {
    const api = new Api()
    const data = await api.get("/analyze/experience-impact")
    setDataPlot(data.dataframe)
  }
  
  useEffect(() => {
    getPlotData()
  }, [])

  return (
    <main className="w-[80%] p-5 float-right">
      <h1 className="text-3xl">
        GymBoard - Evolucion de la experiencia 
      </h1>
      <p className="py-3">
        En la categoria de la evolucion de la experiencia, podemos visualizar que el indice que mas influye son las calorias quemadas en base a la transicion del individuo con un nivel de experiencia bajo, a un nivel mayor o profesional, siendo este un crecimiento con una correlacion de mas del 60%.
      </p>

      {
        dataPlot.map((data, index) => (
          <Plot 
            key={index}
            data={{
              x: data.x,
              y: data.y,
              labels: data.labels,
              correlation: data.correlation
            }}
          />
        ))
      }
    </main>
  )
}
