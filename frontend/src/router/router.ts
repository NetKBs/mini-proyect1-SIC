
import { createBrowserRouter } from 'react-router-dom'
import Layout from '../layout/Layout'
import Home from '../pages/Home';
import Experience from '../pages/Experience';
import Hydratation from '../pages/Hydratation';
import Duration from '../pages/Duration';

export const router = createBrowserRouter([
  {
    path: "/",
    element: Layout({ children: Home() }),
  },
  {
    path: "/analyze/experience-impact",
    element: Layout({ children: Experience() }),
  },
  {
    path: "/analyze/hydration-impact",
    element: Layout({ children: Hydratation() }),
  },
  {
    path: "/analyze/duration-impact",
    element: Layout({ children: Duration() }),
  },
]);