import { install, uninstall } from "@github/hotkey"
import {Controller} from "stimulus";
import * as Turbo from "@hotwired/turbo";

export default class extends Controller {
    static get targets() {
        return ['shortcut']
    }

    connect() {
        install(this.element)
    }

    disconnect() {
        uninstall(this.element)
    }
}
