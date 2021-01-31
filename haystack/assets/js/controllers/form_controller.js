import {Controller} from "stimulus"
import * as Turbo from "@hotwired/turbo"


export default class extends Controller {
    static get targets() {
        return ['submit']
    }

    submitStart() {
        this.disableSubmits()
    }

    disableSubmits() {
        this.submitTargets.forEach(submitTarget => submitTarget.disabled = true)
    }

    submitEnd(event) {
        if (event.detail.success) {
            Turbo.visit(window.location.href)
        }
    }
}
