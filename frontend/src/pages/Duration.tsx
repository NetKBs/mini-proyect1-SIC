import Plot from "../components/Plot"

export default function Duration() {
  return (
    <main className="w-[80%] p-5 float-right">
        <h1 className="text-3xl">
          GymBoard - Duracion de sesiones
        </h1>
        <p className="py-3">
          En este podras encontrar diversos analisis desarrollados a partir de un conjunto de datos recopilados por multiples participantes del fitness, con caracteristicas diferentes como nivel de experiencia, ingesta de agua por litro, frecuencia cardiaca, etc.
        </p>

        <Plot 
          data={{
            title: "No se XD",
            x: ["Principiante", "Intermedio", "Avanzado"],
            y: [726.375, 901.9187192118227, 1265.3403141361257],
            labels: ["Niveles de experiencia", "Calorias quemadas"],
            correlation: 69.41
          }}
        />
      </main>
  )
}
