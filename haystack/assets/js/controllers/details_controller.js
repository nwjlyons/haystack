import { Controller } from "stimulus"


export default class extends Controller {

  static get targets() {
      return ['input']
  }

  disconnect() {
      this.close()
  }

  closeOnClickOutside(event) {
      if (this.element.contains(event.target)) return
      this.close()
  }

  closeOnEscape(keyboardEvent) {
      if (keyboardEvent.key === 'Escape') {
          this.close()
      }
  }

  open() {
      this.element.open = true;
  }

  close() {
      this.element.open = false;
  }

  toggle() {
      this.element.open = !this.element.open;
  }

  update() {
      if (this.hasInputTarget) {
          this.inputTarget.focus()
      }
  }
}
