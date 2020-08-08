import React from 'react'
import App from './components/app'
import Index from './components/index'
import NoMatch from './components/404'
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'

const Routes = () => (
  <Router>
    <App>
      <Switch>
        <Route path='/' exact>
          <Index />
        </Route>
        <Route status={404} component={NoMatch} />
      </Switch>
    </App>
  </Router>
)

export default Routes
