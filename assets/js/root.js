import '../scss/style.scss'
import React from 'react'
import ReactDOM from 'react-dom'
import Routes from './routes'

const rootElem = document.getElementById('root')

if (rootElem) {
  ReactDOM.render(<Routes />, rootElem)
}
