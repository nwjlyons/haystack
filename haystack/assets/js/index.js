import css from "../css/index.css"

import * as Turbo from "@hotwired/turbo"
window['Turbo'] = Turbo

import { Application } from "stimulus"
import { definitionsFromContext } from "stimulus/webpack-helpers"

const application = Application.start()
const context = require.context("./controllers", true, /\.js$/)
application.load(definitionsFromContext(context))
