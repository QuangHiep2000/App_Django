import tw, {styled, theme, css} from 'twin.macro';

export const StyledButton = styled.div(({checkLike}) =>[
  tw` px-1 hover:text-blue-500 flex justify-center items-center cursor-pointer`,
  // css`
  //   &:hover {
  //     font-size: 1.1rem;
  //   }
  // `,
  checkLike && (css`&{color: #2781dd}, &:hover{font-size: 1rem;}`)
]);