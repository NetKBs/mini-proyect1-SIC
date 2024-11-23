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
        En la relación del nivel de ingesta de agua, podemos notar que una ingesta alta de agua influye moderadamente a la quema de calorías en los miembros de gimnasio. Sin embargo al tener una correlación no tan fuerte de 35% , otros factores participan en esta quema de calorías
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
