'use strict';

var myModalEl = document.getElementById('delete-order-modal')
myModalEl.addEventListener('show.bs.modal', function (event) {
    let form = this.querySelector('form');
    form.action = event.relatedTarget.dataset.url;

    let userNameElement = document.getElementById('order-name');
    userNameElement.innerHTML = event.relatedTarget.closest('tr').querySelector('.order-title').textContent;
})