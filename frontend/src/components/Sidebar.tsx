import { Button } from '@nextui-org/react'
import { Link } from 'react-router-dom'
import { SIDEBAR_ITEMS } from "../constants/sidebar.constants";

export default function Sidebar() {
  return (
    <aside className='w-[20%] h-screen bg-slate-700 fixed'>
            <h2 className='text-2xl p-4'>
              <Link to="/">
                  GymBoard
              </Link>
            </h2>
      {
        SIDEBAR_ITEMS.map((item, index) => (
          <Link to={item.link} key={index}>
            <Button className='my-3 w-[90%] mx-3 bg-slate-600 text-white transition-all duration-500 hover:bg-slate-800'>
              { item.label }
            </Button>
          </Link>
        ))
      }
    </aside>
  )
}
