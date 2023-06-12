const container = document.querySelector('.container');

let timeoutIdTitle;
let timeoutIdImg

fetch('scripts/lista.json')
  .then(response => response.json())
  .then(data => {
    data.forEach(item => {
      const div = document.createElement('div');
      div.classList.add('anime');

      const img = document.createElement('img');
      img.classList.add('anime-img');
      img.src = item.imagen;
      img.alt = item.titulo;

      const a = document.createElement('a');
      a.href = item.enlace;
      a.target = '_blank';

      const divTitle = document.createElement('div');
      divTitle.setAttribute('class', 'divTitle');

      const span = document.createElement('span');
      // Limitar la longitud del título a un máximo de 20 caracteres
      const maxTitleLength = 35;
      span.textContent = item.titulo.length > maxTitleLength ? item.titulo.slice(0, maxTitleLength) + '...' : item.titulo + " ";
      span.textContent = span.textContent + " " + item.capitulo;

      divTitle.appendChild(span);

      a.appendChild(img);
      div.appendChild(a);
      div.appendChild(divTitle);
      container.appendChild(div);

    });
  });