import Sidebar from "./components/Sidebar/Index"

export default function App() {
  return (
    <div className="flex">
      <Sidebar />
      <main className="w-[80%] p-5 float-right">
        <h1 className="text-3xl">
          GymBoard - Analisis completo sobre entrenamiento fisico
        </h1>
        <p className="py-3">
          En este podras encontrar diversos analisis desarrollados a partir de un conjunto de datos recopilados por multiples participantes del fitness, con caracteristicas diferentes como nivel de experiencia, ingesta de agua por litro, frecuencia cardiaca, etc.
        </p>
      </main>
    </div>
  )
}
