import { render, screen } from "@testing-library/react";
import ForgetPassword from "../components/ForgetPassword/forgetPassword";


// test("renders Username element on the form", () => {
//   render(<ForgetPassword />);
//   expect(screen.getByText(/Username:/i)).toBeInTheDocument();
// });

test("render button element", () => {
  render(<ForgetPassword />);
  expect(screen.getByText(/Submit/i)).toBeInTheDocument();
});


test("button not absent as an element", () => {
    render(<ForgetPassword />);
    expect(screen.getByText(/Submit/i)).not.toBeNull();
  });


test("render a link  element", () => {
  render(<ForgetPassword />);
  expect(screen.getByText(/Forgot Password/i)).toBeInTheDocument();
});


test("does not render a bouncer text", () => {
    render(<ForgetPassword />);
    expect(screen.getByText(/Forgot Password/i)).not.toBeNull();
  });
