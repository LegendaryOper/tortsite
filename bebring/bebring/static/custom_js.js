document.addEventListener('DOMContentLoaded', () => {
    const links = { '/': '#first', '/category/': '#second', '/about_us': '#third', '/make_offer': '#fourth',
                    '/send_problem': '#fourth'}
    let id;
    for (let key in links) {
        if(location.pathname.includes(key)) id = links[key]
    }
    const link = document.querySelector(id)
    link.classList.add('active')
})