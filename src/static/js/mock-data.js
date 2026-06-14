const products = [
    {
        id: 1,
        name: "MacBook Pro 16",
        description: "Apple M4 Pro chip, 18GB RAM, 512GB SSD",
        price: 2499,
        category: "Mac",
        image_url: "https://picsum.photos/400/250?random=11"
    },
    {
        id: 2,
        name: "iPhone 16 Pro",
        description: "6.3-inch display, A18 Pro chip",
        price: 1199,
        category: "iPhone",
        image_url: "https://picsum.photos/400/250?random=12"
    },
    {
        id: 3,
        name: "iPad Air",
        description: "11-inch display with M3 chip",
        price: 799,
        category: "iPad",
        image_url: "https://picsum.photos/400/250?random=13"
    },
    {
        id: 4,
        name: "Apple Watch Series 10",
        description: "Advanced fitness and health tracking",
        price: 499,
        category: "Watch",
        image_url: "https://picsum.photos/400/250?random=14"
    },
    {
        id: 5,
        name: "AirPods Pro 2",
        description: "Active Noise Cancellation and Spatial Audio",
        price: 249,
        category: "Accessories",
        image_url: "https://picsum.photos/400/250?random=15"
    },
    {
        id: 6,
        name: "Magic Keyboard",
        description: "Wireless keyboard with Touch ID",
        price: 179,
        category: "Accessories",
        image_url: "https://picsum.photos/400/250?random=16"
    }
];

const productsContainer =
    document.getElementById("productsContainer");

function renderProducts(productsList) {

    productsContainer.innerHTML = "";

    if (productsList.length === 0) {

        productsContainer.innerHTML = `
    
        <div class="col-12">

            <div class="alert alert-info text-center">

                <h4>No products found</h4>

                <p class="mb-0">
                    🔍 Please try changing your search query or category filter.
                </p>

            </div>

        </div>
    
    `;

        return;
    }

    productsList.forEach(product => {

        productsContainer.innerHTML += `
        
        <div class="col-lg-4 col-md-6 col-12 mb-4">
        
            <div class="card h-100 shadow-sm">

                <img
                    src="${product.image_url}"
                    class="card-img-top"
                    alt="${product.name}"
                >

                <div class="card-body d-flex flex-column">

                    <h5 class="card-title">
                        ${product.name}
                    </h5>

                    <span class="badge bg-secondary mb-2">
                        ${product.category}
                    </span>

                    <p class="fw-bold">
                        $${product.price}
                    </p>

                    <p class="card-text">
                        ${product.description}
                    </p>

                    <div class="mt-auto">

                    <button
                      class="btn btn-danger btn-sm"
                      data-bs-toggle="modal"
                      data-bs-target="#deleteModal"
                    >
                     Delete
                    </button>

                    <a
                        href="/edit/${product.id}"
                        class="btn btn-warning btn-sm"
                    >
                        Edit
                    </a>
                    
                    <a
                      href="/product/${product.id}"
                      class="btn btn-outline-primary btn-sm"
                    >
                      Details
                    </a>

                    </div>

                </div>

            </div>

        </div>
        
        `;
    });
}

renderProducts(products);

const searchInput = document.getElementById("searchInput");
const categoryFilter = document.getElementById("categoryFilter");

function filterProducts() {

    const searchText =
        searchInput.value.toLowerCase();

    const selectedCategory =
        categoryFilter.value;

    const filteredProducts = products.filter(product => {

        const matchesSearch =
            product.name
                .toLowerCase()
                .includes(searchText);

        const matchesCategory =
            selectedCategory === "all" ||
            product.category === selectedCategory;

        return matchesSearch && matchesCategory;
    });

    renderProducts(filteredProducts);
}

searchInput.addEventListener(
    "input",
    filterProducts
);

categoryFilter.addEventListener(
    "change",
    filterProducts
);