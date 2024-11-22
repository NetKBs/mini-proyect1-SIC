import { BrowserRouter, Routes, Route } from "react-router-dom"
import Home from "./pages/Home"
import Layout from "./layout/Layout"
import Experience from "./pages/Experience"
import Hydratation from "./pages/Hydratation"
import Duration from "./pages/Duration"
import BMP from "./pages/BMP"
import Frecuency from "./pages/Frecuency"

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route 
          path="/" 
          element={
            <Layout>
              <Home />
            </Layout>
          } 
        />
        <Route 
          path="/analyze/experience-impact" 
          element={
            <Layout>
              <Experience />
            </Layout>
          } 
        />
        <Route 
          path="/analyze/hydration-impact" 
          element={
            <Layout>
              <Hydratation />
            </Layout>
          } 
        />
        <Route 
          path="/analyze/duration-impact" 
          element={
            <Layout>
              <Duration />
            </Layout>
          } 
        />
        <Route 
          path="/analyze/bmi-impact" 
          element={
            <Layout>
              <BMP />
            </Layout>
          } 
        />
        <Route 
          path="/analyze/frecuency-impact" 
          element={
            <Layout>
              <Frecuency />
            </Layout>
          } 
        />
      </Routes>
    </BrowserRouter>
  )
}
