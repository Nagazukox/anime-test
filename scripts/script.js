const container = document.querySelector('.container');

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

      a.appendChild(img);
      div.appendChild(a);
      container.appendChild(div);

      // Agregar eventos 'mouseenter' y 'mouseleave' a las imágenes
      img.addEventListener('mouseenter', e => {
        console.log('Encima de la imagen de: ' + e.target.alt);
        img.classList.add('anime-hover');
        img.classList.remove('anime-img');
      });

      img.addEventListener('mouseleave', e => {
        console.log('Fuera de la imagen de: ' + e.target.alt);
        img.classList.remove('anime-hover');
        img.classList.add('anime-img');
      });
    });
  });