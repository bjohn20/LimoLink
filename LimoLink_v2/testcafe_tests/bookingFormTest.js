import { Selector, ClientFunction } from "testcafe";

// Function to get a random element from an array
const getRandomElement = (arr) => arr[Math.floor(Math.random() * arr.length)];

// Function to get a random datetime from today to the end of 2025
const getRandomDateTime = () => {
  const today = new Date();
  const endOfYear = new Date("2025-12-31T23:59");

  const randomTimestamp =
    today.getTime() + Math.random() * (endOfYear.getTime() - today.getTime());
  const randomDate = new Date(randomTimestamp);

  // Format as 'YYYY-MM-DDTHH:MM' for datetime-local input
  const formattedDate = randomDate.toISOString().slice(0, 16);
  return formattedDate;
};

const pickUpAddresses = [
  { street: "123 Main St", city: "Atlanta", state: "GA", zip: "30301" },
  { street: "456 Oak Ave", city: "Savannah", state: "GA", zip: "31401" },
  { street: "789 Pine Rd", city: "Augusta", state: "GA", zip: "30901" },
  { street: "321 Maple Dr", city: "Columbus", state: "GA", zip: "31901" },
  { street: "654 Cedar Ln", city: "Macon", state: "GA", zip: "31201" },
  { street: "987 Elm St", city: "Athens", state: "GA", zip: "30601" },
  { street: "111 Peach Blvd", city: "Roswell", state: "GA", zip: "30075" },
  { street: "222 Magnolia Ct", city: "Albany", state: "GA", zip: "31701" },
  { street: "333 Dogwood Way", city: "Marietta", state: "GA", zip: "30060" },
  { street: "444 River Rd", city: "Valdosta", state: "GA", zip: "31601" },
  {
    street: "555 Willow Pkwy",
    city: "Warner Robins",
    state: "GA",
    zip: "31088",
  },
  { street: "666 Ash St", city: "Johns Creek", state: "GA", zip: "30022" },
  { street: "777 Birch Ave", city: "Sandy Springs", state: "GA", zip: "30328" },
  {
    street: "888 Poplar Ln",
    city: "Peachtree City",
    state: "GA",
    zip: "30269",
  },
  { street: "999 Sycamore St", city: "Cumming", state: "GA", zip: "30040" },
];

const dropOffAddresses = [
  { street: "123 Elm Street", city: "Atlanta", state: "GA", zip: "30301" },
  { street: "456 Oak Avenue", city: "Savannah", state: "GA", zip: "31401" },
  { street: "789 Pine Road", city: "Augusta", state: "GA", zip: "30901" },
  { street: "101 Maple Drive", city: "Macon", state: "GA", zip: "31201" },
  { street: "202 Birch Lane", city: "Columbus", state: "GA", zip: "31901" },
  { street: "303 Cedar Court", city: "Athens", state: "GA", zip: "30601" },
  {
    street: "404 Walnut Street",
    city: "Alpharetta",
    state: "GA",
    zip: "30004",
  },
  { street: "505 Spruce Avenue", city: "Marietta", state: "GA", zip: "30060" },
  { street: "606 Chestnut Road", city: "Roswell", state: "GA", zip: "30075" },
  { street: "707 Redwood Street", city: "Duluth", state: "GA", zip: "30096" },
  {
    street: "808 Poplar Drive",
    city: "Sandy Springs",
    state: "GA",
    zip: "30328",
  },
  {
    street: "909 Sycamore Lane",
    city: "Johns Creek",
    state: "GA",
    zip: "30022",
  },
  {
    street: "111 Ash Street",
    city: "Lawrenceville",
    state: "GA",
    zip: "30046",
  },
  {
    street: "222 Beech Avenue",
    city: "Peachtree City",
    state: "GA",
    zip: "30269",
  },
  { street: "333 Dogwood Road", city: "Kennesaw", state: "GA", zip: "30144" },
];

// Function to get a random address from the pickUpAddresses and dropOffAddresses arrays
const getRandomAddress = (pickUpAddresses, dropOffAddresses) => {
  const randomPickup = getRandomElement(pickUpAddresses);
  const randomDropOff = getRandomElement(dropOffAddresses);

  return {
    pickup: randomPickup,
    dropoff: randomDropOff,
  };
};

// Function to select a random option from a dropdown
const selectRandomOption = async (t, selector) => {
  const options = selector.find("option");
  const optionCount = await options.count;

  if (optionCount > 1) {
    const randomIndex = Math.floor(Math.random() * (optionCount - 1) + 1);
    const randomOption = options.nth(randomIndex);

    await t
      .click(selector) // 1. Click the dropdown to expand it
      .wait(500) // 2. Optional wait for any animations
      .click(randomOption); // 3. Select the random option
  } else if (optionCount === 1) {
    await t.click(options.nth(0));
  }
};

// Function to get a random number between min and max
const getRandomNumber = (min, max) =>
  Math.floor(Math.random() * (max - min + 1) + min);

// Specify the range for random passengers and fare
const getRandomPassengers = () => getRandomNumber(1, 5);
const getRandomFare = () => getRandomNumber(30, 300);

// Function to navigate to the booking form
const navigateToForm = ClientFunction(() => {
  window.location.href = "http://127.0.0.1:8000/bookings/create/";
});

// Function to naviget to the bookings list
const navigateToBookingsList = ClientFunction(() => {
  window.location.href = "http://127.0.0.1:8000/bookings/";
});

// Function to fill out address fields
const fillAddressFields = async (t, address, selectors) => {
  await t
    .click(selectors.street)
    .typeText(selectors.street, address.street, { replace: true })
    .click(selectors.city)
    .typeText(selectors.city, address.city, { replace: true })
    .click(selectors.state)
    .typeText(selectors.state, address.state, { replace: true })
    .click(selectors.zip)
    .typeText(selectors.zip, address.zip, { replace: true });
};

// Function to check pagination
const checkPagination = async (t) => {
  const paginationNext = Selector("a").withText("Next");
  const bookingItems = Selector("#booking-item");

  let page = 1;
  let totalItems = 0;

  // Count items on the first page
  let itemCount = await bookingItems.count;
  totalItems += itemCount;
  console.log(
    `Found ${itemCount} bookings on page ${page}. Total bookings: ${totalItems}`
  );

  // Continue to the next page if the Next button exists and is visible
  while ((await paginationNext.exists) && (await paginationNext.visible)) {
    console.log(`Clicking next on page ${page}`);

    await t.click(paginationNext);

    await t.wait(1000);

    itemCount = await bookingItems.count;
    totalItems += itemCount;
    page++;

    console.log(
      `Found ${itemCount} bookings on page ${page}. Total bookings: ${totalItems}`
    );
  }

  console.log(`Total bookings: ${page} pages: ${totalItems}`);
};

// Testcafe test
fixture`Booking Form Test`.page`http://127.0.0.1:8000/bookings/create/`;

pickUpAddresses.forEach((pickUpAddress, index) => {
  const dropOffAddress = dropOffAddresses[index];

  test(`Submit form for Pickup: ${pickUpAddresses[index].street}, Dropoff: ${dropOffAddress.street}`, async (t) => {
    // Selectors
    const clientDropdown = Selector("#id_client");
    const driverDropdown = Selector("#id_driver");
    const airlineDropdown = Selector("#id_airline");
    const paymentMethodDropDown = Selector("#id_payment_method");
    const submitButton = Selector("button[type='submit']");
    const pickupTime = Selector("#id_pickup_time");
    const selectPassengers = Selector("#id_passengers");
    const selectFare = Selector("#id_fare");

    // Address Selectors
    const pickupSelectors = {
      street: Selector("#id_pickup_street_address"),
      city: Selector("#id_pickup_city"),
      state: Selector("#id_pickup_state"),
      zip: Selector("#id_pickup_zip_code"),
    };

    const dropoffSelectors = {
      street: Selector("#id_dropoff_street_address"),
      city: Selector("#id_dropoff_city"),
      state: Selector("#id_dropoff_state"),
      zip: Selector("#id_dropoff_zip_code"),
    };

    // Select the Random Address
    const randomAddress = getRandomAddress(pickUpAddresses, dropOffAddresses);

    // Get a random date and time
    const randomDateTime = getRandomDateTime();

    // Get random passengers and fare
    const passengers = getRandomPassengers();
    const fare = getRandomFare();

    // Check if the client dropdown exists and is visible
    await t
      .expect(clientDropdown.exists)
      .ok("Client dropdown not found")
      .expect(clientDropdown.visible)
      .ok("Client dropdown is not visible");
    await selectRandomOption(t, clientDropdown);

    // Check if the client dropdown exists and is visible
    await t
      .expect(driverDropdown.exists)
      .ok("Driver dropdown not found")
      .expect(driverDropdown.visible)
      .ok("Driver dropdown is not visible");
    await selectRandomOption(t, driverDropdown);

    // Fill out the address fields
    await fillAddressFields(t, randomAddress.pickup, pickupSelectors);
    await fillAddressFields(t, randomAddress.dropoff, dropoffSelectors);

    // Fill out the rest of the form
    await t
      .click(pickupTime)
      .typeText(pickupTime, randomDateTime, { replace: true });

    await selectRandomOption(t, airlineDropdown);

    await t
      .click(selectPassengers)
      .typeText(selectPassengers, passengers.toString(), { replace: true });

    await t
      .click(selectFare)
      .typeText(selectFare, fare.toString(), { replace: true });

    await selectRandomOption(t, paymentMethodDropDown);

    // Submit the form
    await t.click(submitButton).wait(1000);

    await t.debug();

    await navigateToBookingsList();

    await t.expect(Selector("body").exists).ok("Page didn't load.");

    await t
      .expect(Selector("#booking-item").exists)
      .ok("Booking list didn't load.");

    await checkPagination(t);

    await navigateToForm();
  });
});
