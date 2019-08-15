let aberto = false;
const sidebar = document.getElementById('sidebar');

let sidebarWidth = '250px'
const abrirmenu = () => {
    if (aberto){                
        aberto = false;
        sidebar.style.right = `-${sidebarWidth}`;
        
    } else {                
        sidebar.style.right = '0';
        aberto = true;
    }
}

sidebar.addEventListener('click', abrirmenu)
