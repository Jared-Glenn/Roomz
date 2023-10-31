document.addEventListener('DOMContentLoaded', function() {
    const days = ["today", "day2", "day3", "day4"];
    days.forEach((day, index) => {
        populateHours(document.getElementById(day), index);
    });

    const mockDB = [
        { day: 0, hour: 8, minute: 30, content: "Meeting A" },
        { day: 1, hour: 10, minute: 0, content: "Event B" },
        // ... add more events as needed
    ];

    mockDB.forEach(event => {
        placeEvent(event);
    });
});

function populateHours(dayElement, dayOffset) {
    for (let i = 8; i <= 23; i += 0.5) {
        const hour = document.createElement("div");
        hour.className = "hour";
        hour.dataset.time = i;
        hour.dataset.day = dayOffset;
        if (i % 1 === 0) {
            hour.textContent = `${i}:00`;
        }
        dayElement.appendChild(hour);
    }
}

function placeEvent(event) {
    const day = document.getElementById(days[event.day]);
    const hours = Array.from(day.getElementsByClassName("hour"));
    const targetHour = hours.find(hour => parseFloat(hour.dataset.time) === event.hour + event.minute / 60);
    targetHour.textContent = event.content;
    targetHour.classList.add("event");
}