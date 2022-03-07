import { render, screen } from '@testing-library/react';
import AppEditBlog from "./App";

test('renders learn react link', () => {
  render(<AppEditBlog />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
