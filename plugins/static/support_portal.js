const F = { status: "all", category: "all", sentiment: "all" };

document.querySelectorAll(".fbtn").forEach((b) =>
    b.addEventListener("click", () => {
        const g = b.dataset.g;
        const v = b.dataset.v;
        F[g] = v;
        b.closest(".fg")
            .querySelectorAll(".fbtn")
            .forEach((x) => x.classList.remove("active"));
        b.classList.add("active");
        document.querySelectorAll(".card").forEach((c) => {
            c.style.display =
                (F.status === "all" || c.dataset.status === F.status) &&
                (F.category === "all" || c.dataset.category === F.category) &&
                (F.sentiment === "all" || c.dataset.sentiment === F.sentiment)
                    ? ""
                    : "none";
        });
    })
);
