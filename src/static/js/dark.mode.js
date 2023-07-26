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

    document.addEventListener('DOMContentLoaded', () => {
      const darkModeToggle = document.getElementById('dark-mode-toggle');
      const logoLight = document.getElementById('logo-light');
      const logoDark = document.getElementById('logo-dark');
      const body = document.body;
    
      // Função para atualizar o tema com base na preferência do usuário
      function updateTheme() {
        const theme = localStorage.getItem('theme');
        if (theme === 'dark') {
          body.classList.add('dark-mode');
          darkModeToggle.textContent = 'Ativar Light Mode';
          logoLight.style.display = 'none';
          logoDark.style.display = 'block';
        } else {
          body.classList.remove('dark-mode');
          darkModeToggle.textContent = 'Ativar Dark Mode';
          logoLight.style.display = 'block';
          logoDark.style.display = 'none';
        }
      }
    
      // Adicionar o evento de clique para alternar entre dark mode e light mode, além de salvar a preferência no localStorage
      darkModeToggle.addEventListener('click', () => {
        if (body.classList.contains('dark-mode')) {
          localStorage.setItem('theme', 'light');
        } else {
          localStorage.setItem('theme', 'dark');
        }
        updateTheme();
      });
    
      // Chamar a função de atualização do tema para aplicar a preferência do usuário ao carregar a página
      updateTheme();
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