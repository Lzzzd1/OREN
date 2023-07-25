(function () {
      'use strict'

      var forms = document.querySelectorAll('.needs-validation')

      Array.prototype.slice.call(forms)
        .forEach(function (form) {
          form.addEventListener('submit', function (event) {
            if (!form.checkValidity()) {
              event.preventDefault()
              event.stopPropagation()
            }

            form.classList.add('was-validated')
          }, false)
        })
    })()

    const darkModeToggle = document.getElementById('dark-mode-toggle');
    const logoLight = document.getElementById('logo-light');
    const logoDark = document.getElementById('logo-dark');

    darkModeToggle.addEventListener('click', () => {
      localStorage.setItem('theme', 'dark');
      const body = document.body;
      body.classList.toggle('dark-mode');
      if (body.classList.contains('dark-mode')) {
        darkModeToggle.textContent = 'Ativar Light Mode';
        logoLight.style.display = 'none';
        logoDark.style.display = 'block';
      } else {
      localStorage.setItem('theme', 'light');
        darkModeToggle.textContent = 'Ativar Dark Mode';
        logoLight.style.display = 'block';
        logoDark.style.display = 'none';
      }
    });

    const sidebarDegradeToggle = document.getElementById('sidebar-degrade-toggle');
    const leftSidebar = document.querySelector('.left-sidebar');

    sidebarDegradeToggle.addEventListener('click', () => {
      leftSidebar.classList.toggle('sidebar-degrade');

      if (leftSidebar.classList.contains('sidebar-degrade')) {
        sidebarDegradeToggle.textContent = 'Ativar Degradê';
      } else {
        sidebarDegradeToggle.textContent = 'Tirar Degradê';
      }
    });