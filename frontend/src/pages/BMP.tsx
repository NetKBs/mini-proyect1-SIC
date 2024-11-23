import Plot from "../components/Plot"
import { useEffect, useState } from "react"
import { Api } from "../services/Api"
import { Dataframe } from "../interfaces/api.interface"

export default function BMP() {
  const [dataPlot, setDataPlot] = useState<Dataframe[]>([] as Dataframe[])

  const getPlotData = async () => {
    const api = new Api()
    const data = await api.get("/analyze/bmi-impact")
    setDataPlot(data.dataframe)
  }
  
  useEffect(() => {
    getPlotData()
  }, [])

  return (
    <main className="w-[80%] p-5 float-right">
      <h1 className="text-3xl">
        GymBoard - Frecuencia cardiaca (BMP)
      </h1>
      <p className="py-3">
        Se puede ver en la gráfica que las personas con mayor masa corporal tienden a quemar más calorías en comparación con aquellas con menor masa corporal, pero es importante hacer notar que el BMI no distingue entre masa muscular y masa grasa por lo que una persona con un BMI alto debido a una mayor masa muscular puede tener un gasto calórico diferente en comparación con alguien con un BMI alto debido a una mayor cantidad de grasa corporal.
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
