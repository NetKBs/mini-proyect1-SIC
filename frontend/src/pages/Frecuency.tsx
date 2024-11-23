import Plot from "../components/Plot"
import { useEffect, useState } from "react"
import { Api } from "../services/Api"
import { Dataframe } from "../interfaces/api.interface"

export default function Frecuency() {
  const [dataPlot, setDataPlot] = useState<Dataframe[]>([] as Dataframe[])

  const getPlotData = async () => {
    const api = new Api()
    const data = await api.get("/analyze/frecuency-impact")
    setDataPlot(data.dataframe)
  }
  
  useEffect(() => {
    getPlotData()
  }, [])

  return (
    <main className="w-[80%] p-5 float-right">
      <h1 className="text-3xl">
        GymBoard - Frecuencia de entrenamiento
      </h1>
      <p className="py-3">
        Como se puede apreciar en la gráfica cuanto mas días se haga mas bajo estará el porcentaje de grasa corporal, haciendo una observación aun que con 5 días sea el mas bajo no es del todo recomendado no al menos para las mujeres ya que, el porcentaje de grasa ideal en mujeres es del 14% al 31% mientras que en los hombres es del 6% al 24% entonces la recomendación es que en el caso de las mujeres se haga 4 o 5 días y el hombres se priorice hacer 5 días
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
