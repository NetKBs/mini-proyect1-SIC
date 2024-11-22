import Plot from "../components/Plot"
import { useEffect, useState } from "react"
import { Api } from "../services/Api"
import { Dataframe } from "../interfaces/api.interface"

export default function Hydratation() {
  const [dataPlot, setDataPlot] = useState<Dataframe[]>([] as Dataframe[])

  const getPlotData = async () => {
    const api = new Api()
    const data = await api.get("/analyze/hydration-impact")
    setDataPlot(data.dataframe)
  }
  
  useEffect(() => {
    getPlotData()
  }, [])

  return (
    <main className="w-[80%] p-5 float-right">
      <h1 className="text-3xl">
        GymBoard - Ingesta de agua
      </h1>
      <p className="py-3">
        En este podras encontrar diversos analisis desarrollados a partir de un conjunto de datos recopilados por multiples participantes del fitness, con caracteristicas diferentes como nivel de experiencia, ingesta de agua por litro, frecuencia cardiaca, etc.
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
