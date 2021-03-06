let name = ['Benedito', 'Augusto', 'Paula', 'Silvia', 'Miranda']
let rand_cpf
let rand_rg
let rand_cnh
let rand_cep = Math.floor(Math.random() * 1000000)
let rand_phone
let rand_number = Math.floor(Math.random() * 10000)

describe('Input form', () => {
  it('focuses input on load', () => {
    cy.visit('http://localhost:8000/')

    cy.get('input[name="username"]').type('regis')
    cy.get('input[name="password"]').type('d')
    cy.wait(500)
    cy.get('button[type="submit"]').click()

    cy.wait(500)
    cy.get("#id_pessoas").click()
    cy.wait(1000)
    cy.get('.btn-primary').click()
    cy.wait(500)

    var rand_name = name[Math.floor(Math.random() * name.length)]
    cy.get('input[name="nome"]').type(rand_name)
    cy.get('input[name="sobrenome"]').type('Santos')
    cy.get('input[name="apelido"]').type('Cidão')
    cy.get('input[name="mae"]').type('Ivonete Santos')
    cy.get('input[name="pai"]').type('Benedito Santos')
    cy.get('#faccao').select('5')
    cy.wait(500)

    cy.get('#heading2').click()
    rand_cpf = Math.floor(Math.random() * 99999999999)
    cy.get('#id_cpf').type(rand_cpf)
    rand_rg = Math.floor(Math.random() * 99999999999)
    cy.get('#id_rg').type(rand_rg)
    rand_cnh = Math.floor(Math.random() * 1000000)
    cy.get('#id_cnh').type(rand_cnh)
    cy.wait(500)

    cy.get('#heading3').click()
    cy.get('#id_address').type('Rua da Glória')
    cy.get('#id_address_number').type(rand_number)
    cy.get('#id_complement').type('4º andar')
    cy.get('#id_district').type('Centro')
    cy.get('#id_city').type('São Paulo')
    cy.get('#uf').select('SP')
    cy.get('#id_cep').type(rand_cep)
    cy.wait(500)

    cy.get('#heading6').click()
    cy.get('#natureza1').select('1')
    cy.get('#qualificacao1').select('aut')
    cy.get('#arma1').select('1')
    cy.get('#status1').select('foragido')
    cy.get('#btnInfracao').click()
    cy.get('#natureza2').select('2')
    cy.get('#qualificacao2').select('aut')
    cy.get('#arma2').select('2')
    cy.get('#status2').select('morto')
    cy.wait(500)

    cy.get('#heading7').click()
    cy.get('#ocorrencia1').select('1')
    cy.get('#btnOcorrencia').click()
    cy.get('#ocorrencia2').select('2')
    cy.wait(500)

    cy.get('#heading8').click()
    cy.get('#tipo1').select('cel')
    rand_phone = Math.floor(Math.random() * 10000000000)
    cy.get('#telefone1').type(rand_phone)
    cy.get('#btnContato').click()
    cy.get('#tipo2').select('cel')
    rand_phone = Math.floor(Math.random() * 10000000000)
    cy.get('#telefone2').type(rand_phone)
    cy.wait(500)

    cy.get('#heading9').click()
    cy.get('#comparsa_nome1').type('André')
    rand_cpf = Math.floor(Math.random() * 999999999999)
    cy.get('#comparsa_cpf1').type(rand_cpf)
    rand_rg = Math.floor(Math.random() * 100000000000)
    cy.get('#comparsa_rg1').type(rand_rg)
    rand_cnh = Math.floor(Math.random() * 1000000)
    cy.get('#comparsa_cnh1').type(rand_cnh)
    cy.get('#btnComparsa').click()
    cy.get('#comparsa_nome2').type('Pedro')
    rand_cpf = Math.floor(Math.random() * 10000000000)
    cy.get('#comparsa_cpf2').type(rand_cpf)
    rand_rg = Math.floor(Math.random() * 100000000000)
    cy.get('#comparsa_rg2').type(rand_rg)
    rand_cnh = Math.floor(Math.random() * 1000000)
    cy.get('#comparsa_cnh2').type(rand_cnh)

    cy.get('#heading10').click()
    cy.get('#veiculo1').select('1')
    cy.get('#btnVeiculo').click()
    cy.get('#veiculo2').select('2')

    cy.get('button[type="submit"]').click()
  })
})
