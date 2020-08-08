import React from 'react'
import { theme } from '../theme'
import ThemeProvider from '@material-ui/styles/ThemeProvider'

const App = props => (
  <ThemeProvider theme={theme}>
    <h2>I'm a pretty Master</h2>
    {props.children}
  </ThemeProvider>
)

export default App
